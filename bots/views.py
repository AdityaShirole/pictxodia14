from django.shortcuts import render_to_response, render, HttpResponseRedirect
from bots.models import Author, Bot, Log
from django.template import RequestContext
from bots.forms import SignUp, Login, UploadBot
import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from XOdia import settings
from django.core.files import File
import re
from XOdia.settings import BASE_DIR
# Create your views here.

@csrf_exempt
def bots_home(request, opt = 0):
	opt = int(opt)
	login_status = 0
	user = ''
	if 'username' in request.session:
		form = UploadBot()
		login_status = 1
		opt = 3
		user = request.session['username']
	elif opt == 1 :
		form = Login()
	elif opt == 2:
		form = SignUp()
	else:
		form = None		
	temp = "{"
	for bot in Bot.objects.all():
		temp = temp + "'" + bot.Name + "'" + ":" + str(bot.id) + ","
	temp = temp+"}"
	bot_name_id = eval(temp)
	return render_to_response(
		'index.html',
		{
			'login_status': login_status,
			'form': form,
			'bot_name_id': bot_name_id,
			'opt': opt,
			'user': user,
		},
		context_instance = RequestContext(request)
	)

@csrf_exempt
def sign_up(request):
	if request.method == 'POST':
		form = SignUp(request.POST, request.FILES)
		if form.is_valid():
			if not Author.objects.filter(username = request.POST['username']).exists():
				username = form.cleaned_data['username']
				Name = form.cleaned_data['Name']
				Contact = form.cleaned_data['Contact']
				Email = form.cleaned_data['Email']
				password = form.cleaned_data['password']
				rec_datetime = datetime.datetime.now()
				author = Author(
					username = username,
					Name = Name,
					Contact = Contact,
					Email = Email,
					password = password,
					attempts = 0,
				)
				author.save()
				request.POST['username'] = author.username
				request.POST['password'] = author.password
				log_in(request)
			else:
				return render_to_response(
						'message.html',
						{
							'message': 'Failed to create login',
							'meta_message': 'The username you have given is already present.\nPlease try another username.',
						},
						context_instance = RequestContext(request),
					)
	return HttpResponseRedirect('/')

@csrf_exempt
def log_in(request):
	if request.method == 'POST':
   		if Author.objects.filter(username = request.POST['username'], password = request.POST['password']).exists():
   			request.session['username'] = request.POST['username']
   			return HttpResponseRedirect('/bots/mypage/')
			#return HttpResponse("valid")
   		else:
   			return render_to_response(
   					'message.html',
   					{
   						'message': 'Invalid details',
   						'meta_message': 'Failed to log in',
   						'login_status': 1,
   					},
   					context_instance = RequestContext(request),
   				)
	else:
   		form = Login()
   		return render_to_response(
   				'login.html',
   				{'form': form,},
   				context_instance = RequestContext(request),
   			)

def log_out(request):
	if 'username' in request.session:
		del request.session['username']
	return HttpResponseRedirect('/')

@csrf_exempt
def submit_bot(request):
	if request.method == 'POST' and 'username' in request.session:
		author = Author.objects.get(username = request.session['username'])
		try:
			old_bot = author.bot_set.get()
		except:
			old_bot = None
		if author.attempts >= 3:
			return render_to_response(
					'message.html',
					{
						'message': "Can't accept submission.",
						'meta_message': 'Your maximum attempts(3) are already over.',
					},
					context_instance = RequestContext(request),
				)
		else:
			form = UploadBot(request.POST, request.FILES)
			if form.is_valid():
				Name = form.cleaned_data['Name']
				rec_datetime = datetime.datetime.now()
				bot = Bot(
					author = author,
					Name = Name,
					rec_datetime = rec_datetime,
					code = request.FILES['code'],
					wins = 0,
					loss = 0,
					draw = 0,
					ldrbrd_pos = None,
				)
				bot.save()
				author.attempts = author.attempts + 1
				author.save()
				#try:
				if 1:
					bot_handle(bot, old_bot)
					print "just after bot_handle"
					print bot.wins
					print bot.loss
					if old_bot:
						for log in Log.objects.filter(bot1 = old_bot):
							log.winner.wins = log.winner.wins - 1
							log.winner.save()
							log.loser.loss = log.loser.loss-1
							log.loser.save()
						for log in Log.objects.filter(bot2 = old_bot):
							log.winner.wins = log.winner.wins - 1
							log.winner.save()
							log.loser.loss = log.loser.loss-1
							log.loser.save()
						Bot.objects.filter(id = old_bot.id).delete()
						del old_bot
					print " "
					print bot.wins
					print bot.loss
					leaderboard_generator()
					message = 'Your bot has been accepted!'
				#except:
				#	Bot.objects.filter(id = bot.id).delete()
				#	author.attempts = author.attempts - 1
				#	author.save()
				#	message = 'submission failed due to unexpected reason'
				return render_to_response(
						'message.html',
						{
							'message': message,
						},
						context_instance = RequestContext(request),
					)
			else:
				return HttpResponse('invalid')
	else:
		return HttpResponseRedirect('/bots/#login')

def games(request,first,second):
	if 'username' in request.session:
		login_status = 0
	else:
		login_status = 1
	if Bot.objects.filter(id = first).exists() and Bot.objects.filter(id = second).exists():
		first_bot = Bot.objects.get(id = first)
		second_bot = Bot.objects.get(id = second)
		if Log.objects.filter(bot1 = first_bot, bot2 = second_bot).exists():
			log = Log.objects.get(bot1 = first_bot, bot2 = second_bot)
			win = log.winner
			loser = log.loser
			logfile = log.logfile
			logstring = logfile.read()
			bot1 = log.bot1.Name
			bot2 = log.bot2.Name
			return render_to_response(
					'game.html',
					{
						'login_status': login_status,
						'logstring':logstring,
						'bot1': bot1,
						'bot2': bot2,
					 	'win': win,
					 	'loser': loser,	
					},
					context_instance = RequestContext(request)
				)
		else:
			return render_to_response(
					'message.html',
					{
						'message': "Can't display the game.",
						'meta_message': 'Kindly report if you see this page.' ,
					},
					context_instance = RequestContext(request),
				)
	else:
		return render_to_response(
				'message.html',
				{
					'message': 'invalid request',
				},
				context_instance = RequestContext(request),
			)

def leaderboard(request):
	if 'username' in request.session:
		login_status = 0
                current_user = Author.objects.get(username = request.session['username'])
                user = current_user.Name
                username = current_user.username
	else:
		login_status = 1        
                current_user = 	None
                user = None
                username = None
	temp = sorted(Bot.objects.all(), key = lambda x: x.wins, reverse = True)
	leaders = []
	pos = 1
	for bot in temp:
		leaders.append((pos, bot.Name, bot.author.Name, bot.wins))
		pos = pos + 1
	return render_to_response(
		'leaderboard.html',
		{
                        'leaders':leaders, 
                        'login_status': login_status,
                        'user': user,
                        'username': username,
                },
		context_instance = RequestContext(request),
	)

def my_page(request,opt = 0):
	opt = int(opt)
	form = UploadBot()
	current_user = Author.objects.get(username = request.session['username'])
	username = current_user.username
	try:
		bot = Bot.objects.get(author = current_user)
	except:
		bot = None
	temp = sorted(Bot.objects.all(), key = lambda x: x.wins, reverse = True)
	leaders = []
	pos = 1
	for bot in temp:
		if pos <= 3:
			leaders.append((pos, bot.Name, bot.author.Name, bot.wins))
			pos = pos + 1
		else:
			break	
	return render_to_response(
			'logged.html',
			{
				'username':username,
				'form':form,
				'opt':opt,
				'bot':bot,
				'leaders': leaders,
			},
			context_instance = RequestContext(request),
		)

def error(request):
	if 'username' in request.session:
		login_status = 0
	else:
		login_status = 1	
        	
        return render_to_response(
		'message.html',
		{
			'login_status': login_status,
		},
		context_instance = RequestContext(request),
	)
def teamp(request):
	if 'username' in request.session:
		login_status = 0
                username = request.session['username']	
        else:
       		login_status = 1
                username = None 	
	return render_to_response(
		'teamp.html',
		{
                        'username': username,
			'login_status': login_status,
		},
		context_instance = RequestContext(request),
	)

def bot_handle(new_bot, old_bot):
	#this function assumes particular location of judge..
	#errors are possible if application is ported..
	mediapath = settings.BASE_DIR+'/media/'
	botpath = mediapath+'bots/'
	logpath = mediapath+'logfiles/'
	if old_bot:
		old_bot_id = old_bot.id
	else:
		old_bot_id = 0
	for bot in Bot.objects.all():
		if bot.id != new_bot.id and bot.id != old_bot_id:
			os.chdir('JUDGE')
			os.system('echo push1995 | sudo -S python judge_with_run.py '+mediapath+str(new_bot.code)+' '+mediapath+str(bot.code))
			os.chdir('..')
			logfile = str(new_bot.id)+'vs'+str(bot.id)+'.txt'
			os.system('mv ./JUDGE/sachin.txt '+'./JUDGE/'+logfile)#SACHIN.txt is assumed to be in same directory as manage.py
			logfile = BASE_DIR+'/JUDGE/'+logfile
			logfile1 = open(logfile)
			#determining the winner from logfile
			logstring = logfile1.read()
			temp = re.search(r'#.(?P<win>\d)', logstring)
			
			if int(temp.group('win')) == 1:
				print '\n###### won by %s ######\n'%(new_bot.Name)
				winner = new_bot
				loser = bot
				winner.wins = winner.wins+1
				winner.save()
				print winner.wins
				print winner.loss
				loser.loss = loser.loss+1
				loser.save()
				print loser.wins
				print loser.loss
			elif int(temp.group('win')) == 2:
				print '\n###### won by %s ######\n'%(bot.Name)
				winner = bot
				loser = new_bot
				winner.wins = winner.wins+1
				winner.save()
				print winner.wins
				print winner.loss
				loser.loss = loser.loss+1
				loser.save()
				print loser.wins
				print loser.loss
			else:
				winner = None
				loser = None
				bot.draw = bot.draw+1
				bot.save()
				new_bot.draw = new_bot.draw+1
				new_bot.save()
			#done
			logfile2 = File(logfile1)
			print "before saving logs"
			print new_bot.wins
			print new_bot.loss
			log = Log(bot1 = new_bot, bot2 = bot, winner = winner, loser = loser, logfile = logfile2)
			log.save()
			print "after saving logs"
			print new_bot.wins
			print new_bot.loss
			os.system('echo push1995 |sudo -S rm '+logfile)#again logfile is assumed in pwd
	for bot in Bot.objects.all():
		if old_bot:
			old_bot_id = old_bot.id
		else:
			old_bot_id = None
		if bot.id != new_bot.id and bot.id != old_bot_id:
			os.chdir('JUDGE')
			os.system('cp original_grid_bot.txt grid.txt')
			os.system('cp original_grid_valid.txt grid_val.txt')
			os.system('echo push1995 | sudo -S python judge_with_run.py '+mediapath+str(bot.code)+' '+mediapath+str(new_bot.code))
			os.chdir('..')
			logfile = str(bot.id)+'vs'+str(new_bot.id)+'.txt'
			os.system('mv ./JUDGE/sachin.txt '+'./JUDGE/'+logfile)
			logfile = BASE_DIR+'/JUDGE/'+logfile
			logfile1 = open(logfile)
			#determining the winner from logfile
			logstring = logfile1.read()
			temp = re.search(r'#.(?P<win>\d)', logstring)
			if int(temp.group('win')) == 1:
				print '\n###### won by %s ######\n'%(bot.Name)
				winner = bot
				loser = new_bot
				winner.wins = winner.wins+1
				winner.save()
				print winner.wins
				print winner.loss
				loser.loss = loser.loss+1
				loser.save()
				print loser.wins
				print loser.loss
			elif int(temp.group('win')) == 2:
				print '\n###### won by %s ######\n'%(new_bot.Name)
				winner = new_bot
				loser = bot
				winner.wins = winner.wins+1
				winner.save()
				print winner.wins
				print winner.loss
				loser.loss = loser.loss+1
				loser.save()
				print loser.wins
				print loser.loss
			else:
				winner = None
				loser = None
				new_bot.draw = new_bot.draw+1
				new_bot.save()
				bot.draw = bot.draw+1
				bot.save()
			#done
			logfile2 = File(logfile1)
			print "before saving logs"
			print new_bot.wins
			print new_bot.loss
			log = Log(bot1 = bot, bot2 = new_bot, winner = winner, loser = loser, logfile = logfile2)
			log.save()
			print "after saving logs"
			print new_bot.wins
			print new_bot.loss
			os.system('echo push1995 |sudo -S rm '+logfile)
	print "at end of bot_handle"
	print new_bot.wins
	print new_bot.loss


def leaderboard_generator():
	temp = sorted(Bot.objects.all(), key = lambda x: x.wins, reverse = True)
	leaders = []
	pos = 1
	for bot in temp:
		if pos == 1:
			try:
				if leaders[-1][3] == bot.wins:
					leaders.append((pos, bot.Name, bot.author.Name, bot.wins))	
					bot.ldrbrd_pos = pos
					bot.save()
				else:
					pos = pos+1
					leaders.append((pos, bot.Name, bot.author.Name, bot.wins))
					bot.ldrbrd_pos = pos
					bot.save()									
			except:
				leaders.append((pos, bot.Name, bot.author.Name, bot.wins))
				bot.ldrbrd_pos = pos
				bot.save()
		else:
			if leaders[-1][3] == bot.wins:
				leaders.append((pos, bot.Name, bot.author.Name, bot.wins))
				bot.ldrbrd_pos = pos
				bot.save()
			else:
				pos = pos+1
				leaders.append((pos, bot.Name, bot.author.Name, bot.wins))
				bot.ldrbrd_pos = pos
				bot.save()
