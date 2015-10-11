 // Set up the scene, camera, and renderer as global variables.
    var scene, camera, renderer;
	
    var callbacks = new Array();
	var jam="b.7.1.12.12 d.6.9.13.13 k.6.7.14.14";
	var trial = jam.split(" ");
	//Stuff for logfile reading.
	//var log1 = "b.7.1.12.12 b.3.6.13.13"; this is shifted to game.html
	var move;
	var timeout;
	var s;
	var moves = new Array();
	var j=0,h;
	var log2 = log1.split(" ");
	for(var r=0;r<log2.length;r++)
	{
	    move = log2[r].split(".");
		moves[r]=move;
	}
	
	//variables for coordinates and createPiece function
	var xc, zc,piece, d="Dragon" , k= "knight" , b="banner";
	//var log="b.6.12.12.13";
	//var moves=log.split(".");
	var meshPiece=[];
	var initx=[];
	var initz=[];
	var index,count,iaa, number=0;
	//Set squareSize as global variable. YO!
	var squareSize=6.25;
    init();
    animate();

    // Sets up the scene. Time to rock.
    function init() {

        document.getElementById("test").innerHTML =
            "<input type='button' onclick='play()' value = 'Play'>  </input>" + "<input type='button' onclick='pause()' value = 'Pause'></input>"
            + "<input type='button' onclick='nextmove()' value = 'Next'></input>";
	}
    // Create the scene and set the scene size. This is where the magic happens.
    scene = new THREE.Scene();
    var WIDTH = window.innerWidth,
      	HEIGHT = window.innerHeight;

      // Create a renderer and add it to the DOM.
      renderer = new THREE.WebGLRenderer({antialias:true});
      renderer.setSize(WIDTH, HEIGHT);
      document.body.appendChild(renderer.domElement);

      // Create a camera, zoom it out from the model a bit, and add it to the scene. Lights. Camera . Action. this is the camera
      camera = new THREE.PerspectiveCamera(45, WIDTH / HEIGHT, 0.1, 20000);
      camera.position.set(170,90,170); //170,90,170 for a good view
      scene.add(camera);
	 
      // Create an event listener that resizes the renderer with the browser window.
      window.addEventListener('resize', function() {
        var WIDTH = window.innerWidth,
            HEIGHT = window.innerHeight;
        renderer.setSize(WIDTH, HEIGHT);
        camera.aspect = WIDTH / HEIGHT;
        camera.updateProjectionMatrix();
      });

      // Set the background color of the scene.
      renderer.setClearColorHex(0xffffff, 1);

      // Create a light, set its position, and add it to the scene.
      var light = new THREE.DirectionalLight(0xfcfcfc,1.5);
      light.position.set(10,70,10);//originally had .normalize after bracket
      scene.add(light);

	  var light2 = new THREE.PointLight(0xffffff,1);
      light2.position.set(200,400,0);
	  scene.add(light2);
	 
	  //Shadows
	  renderer.shadowMapEnabled = true;
      renderer.shadowMapSoft = false;

      renderer.shadowCameraNear = 3;
      renderer.shadowCameraFar = camera.far;
      renderer.shadowCameraFov = 50;

      renderer.shadowMapBias = 0.0039;
      renderer.shadowMapDarkness = 0.5;
      renderer.shadowMapWidth = 1024;
      renderer.shadowMapHeight = 1024;
	
	light.castShadow = true;

      // Load in the mesh and add it to the scene.
	   var material_black = new THREE.MeshLambertMaterial( { ambient: 0x000000, color: 0x000000 } ); //color: object hexadecimal color after the 0x
	   var material2 = new THREE.MeshLambertMaterial( { ambient: 0x333f47, color: 0x33f47 } ); //color: object hexadecimal color after the 0x
	   var common = new THREE.MeshLambertMaterial( { ambient: 0x082c01, color: 0x082c01 } ); //color: object hexadecimal color after the 0x
	   var throne = new THREE.MeshLambertMaterial( { ambient: 0x8fad89, color: 0x8fad89 } ); //color: object hexadecimal color after the 0x
	   var sidelane1 = new THREE.MeshLambertMaterial( { ambient: 0x673d00, color: 0x673d00 } );
	   var lane1influence = new THREE.MeshLambertMaterial( { ambient: 0xffb400, color: 0xffb400 } );
	   var defense = new THREE.MeshLambertMaterial( { ambient: 0x30f30a, color: 0x30f30a } ); //color: object hexadecimal color after the 0x
	   var sidelane2 = new THREE.MeshLambertMaterial( { ambient: 0x511201, color: 0x511201 } );
	   var lane2influence = new THREE.MeshLambertMaterial( { ambient: 0xfd8261, color: 0xfd8261 } );
	   
	   var squareMaterial;
	// Code for Squares		
	  for (var row = 0; row < 18; row++) {
		    for (var col = 0; col < 18; col++) {
		        /*CHESS TYPE MATERIALS
				if ((row + col) % 2 === 0) { // light square
		            squareMaterial = material1;
		        } else { // dark square
		            squareMaterial = material2;
		        }
				*/
				var height;
				if(  (row==0) || (row==17) )				//row 0 and 17 ke liye
				{
					if( (col<8) || (col>9) )
					{
							height=10;
							squareMaterial=material_black;			//black squares
						
					}
					else if( (col==9) || (col==8) )
					{
						height=30;
						squareMaterial=material2;
					}
					else
					{	
					height=0.0001;
					squareMaterial=material2;
					}
				}
				
				else if(  (row==1) || (row==16) )			//row 1 and 16 ke liye. Aur Banao Camelot... -_-  
				{
					if( (col<3) || (col>=15) )				//black squares
					{
						if( (col==2) || (col==15) )			//dark Green
						{
						height=0.02;
						squareMaterial=common;
						}
						
						
						
						
						else
						{
						height=10;
						squareMaterial=material_black;
						}
					}
					
					else if( (col>3) || (col<15) )
						{
							if( (col==9) || (col==8) )			//throne lane
							{
								height=0.02;
								squareMaterial=throne;
							}
							
							else								//defense area
							{
								height=0.02;
								squareMaterial=defense;
							}
						}
					
					else
					{	
					height=0.0001;
					squareMaterial=material2;
					}
				}
				
				else if(  (row==2) || (row==15) )			//row 2 and 15 ke liye... Aur banao Different Zones.  -_-
				{				
					if( (col<1) || (col>16) )				//black squares
					{
						height=10;
						squareMaterial=material_black;
					}
					else if( (col>1) || (col<16) )
						{
							if( (col==9) || (col==8) )			//throne lane
							{
								height=0.02;
								squareMaterial=throne;
							}
							
							
							else if( (col<3) || (col>14) )	//common area
							{
								height=0.02;
								squareMaterial=common;
							}
							
							else								//defense area
							{
								height=0.02;
								squareMaterial=defense;
							}
						}
					
					else
					{	
					height=0.0001;
					squareMaterial=material2;
					}
				}
				else if(  (row==3) || (row==14) )			//row 3 and 14 ke liye... *@#$#%$ers ...   -_-
				{				
					
					if( (col>1) || (col<16) )
						{
							if( (col==8) || (col==9) )			//throne lane
							{
								height=0.02;
								squareMaterial=throne;
							}
							
							
							else if( (col<3) || (col>14) )	//common area
							{
								height=0.02;
								squareMaterial=common;
							}
							
							else								//defense area
							{
								height=0.02;
								squareMaterial=defense;
							}
						}
					
					else
					{	
					height=0.0001;
					squareMaterial=material2;
					}
				}
				else if(  (row==4) || (row==13) )			//row 4 and 13 ke liye... MOD3 chahiye tha ...   -_-
				{				
					
					if( (col>1) || (col<16) )
						{
							if( (col==8) || (col==9) )			//throne lane
							{
								height=0.02;
								squareMaterial=throne;
							}
							else if( (col<9) || (col>8) )	//common area
							{
								height=0.02;
								squareMaterial=common;
							}
							
						}
					
					else
					{	
					height=0.0001;
					squareMaterial=material2;
					}
				}
				
				else										//remaining rows
				{	
					for(var i=0;i<4;i++)
					{
						if( col<8 )
						{
							if( (col==3) || (col==4) )			//side lane 1
							{
								height=0.02;
								squareMaterial=sidelane1;
							}
							else
							{
								height=0.02;
								squareMaterial=lane1influence;
							}
						}
						
						else if( col>9 )	
						{
							if( (col==13) || (col==14) )
							{
								height=0.02;
								squareMaterial=sidelane2;
							}
							
							else
							{
								height=0.02;
								squareMaterial=lane2influence;
							}
						}
					
						else
						{	
							height=0.0001;
							squareMaterial=material2;
						}
					}
				}
					
			
				
		        var square = new THREE.Mesh(new THREE.CubeGeometry(squareSize, squareSize, height,0),squareMaterial);//add material after 1,1
		 
		        square.position.x = col * squareSize + squareSize / 2;
		        square.position.z = row * squareSize + squareSize / 2;
		        square.position.y = -0.01;
				
		 
		        square.rotation.x = -90 * Math.PI / 180;
				square.receiveShadow=true;
		        scene.add(square);
		    }
		}
		
	  
	//UpdateBoard Function. Works properly. 
	  function updateBoard(piece, rows, cols, finalx, finaly)
	  {

          console.log(rows +" "+cols +" "+ finalx +" "+ finaly)
	for(count=1; count<21 ; count++)
	{	
		if(  (initx[count])==cols)
		{
			if( (initz[count]) ==rows )
			{
				iaa=count;
				console.log("Update Booard Ran");
							//setTimeout(function() {
							scene.remove(meshPiece[iaa]);
							createPiece(iaa,piece,finalx,finaly );
 							animate(); 
			    //}, 3000);
 							//break;
							
            }			
		}			
	}
}//End of updateBoard function
	
	  createPiece(1,d,6,9,0);
	  createPiece(2,k,6,7,0);
	  createPiece(3,k,6,12,0);
	  createPiece(4,b,3,6,0);
	  createPiece(5,b,7,1,0);
	  createPiece(6,b,7,10,0);
	  createPiece(7,b,7,18,0);
	  createPiece(8,k,3,8,0);
	  createPiece(9,b,3,11,0);
	  createPiece(10,b,3,13,0);
	  
	  createPiece(11,d,12,9,1);
	  createPiece(12,k,12,6,1);
	  createPiece(13,k,12,11,1);
	  createPiece(14,b,15,5,1);
	  createPiece(15,b,11,0,1);
	  createPiece(16,b,11,9,1);
	  createPiece(17,b,11,17,1);
	  createPiece(18,k,15,7,1);
	  createPiece(19,b,15,10,1);
	  createPiece(20,b,15,12,1);

	/*

	//This part works properly. Thank You Jam! 
	  //setTimeout(function () {
		setTimeout(function() {
	      updateBoard(b,trial[1],trial[2],trial[3],trial[4]);
		  }, 4000);
		setTimeout(function() {
	      updateBoard(b, 3, 11, 14, 12);
		  }, 9000);
		  setTimeout(function() {
	      updateBoard(b, 14, 12, 16, 14);
		  }, 13000);
*/
	  //}, 1000);


	  //load board
	  var loader2=new THREE.JSONLoader();
	  loader2.load("models/board.js",function(geometry,materials){
	  var material2= new THREE.MeshLambertMaterial(materials);
	  mesh2 = new THREE.Mesh(geometry, new THREE.MeshFaceMaterial(materials) );  
	  mesh2.position.x=56.25;
	  mesh2.position.y=-0.2;//keep as -0.2
	  mesh2.position.z=56.25;
	  mesh2.receiveShadow= true;
	  mesh2.scale.x=50;
	  mesh2.scale.y=50;
	  mesh2.scale.z=50;
	  scene.add(mesh2);
	  } );
	  
	  
	  
	 /* 
	  var CubeHero = new THREE.Mesh(new THREE.CubeGeometry(5, 40, 5,0) );
	  CubeHero.position.x=6*9;
	  CubeHero.position.y=0;
	  CubeHero.position.z=6*2;
	  scene.add(CubeHero);
	  
	  var CubeBanDef1 = new THREE.Mesh(new THREE.CubeGeometry(5, 20, 5,0) );
	  CubeBanDef1.position.x=6*8;
	  CubeBanDef1.position.y=0;
	  CubeBanDef1.position.z=6*2;
	  scene.add(CubeBanDef1);
	  
	  var CubeBanDef2 = new THREE.Mesh(new THREE.CubeGeometry(5, 20, 5,0) );
	  CubeBanDef2.position.x=6*7;
	  CubeBanDef2.position.y=0;
	  CubeBanDef2.position.z=6*2;
	  scene.add(CubeBanDef2);
	  
	  var CubeBanDef3 = new THREE.Mesh(new THREE.CubeGeometry(5, 20, 5,0) );
	  CubeBanDef3.position.x=6*11;
	  CubeBanDef3.position.y=0;
	  CubeBanDef3.position.z=6*2;
	  scene.add(CubeBanDef3);
	  
	  var CubeBanDef4 = new THREE.Mesh(new THREE.CubeGeometry(5, 20, 5,0) );
	  CubeBanDef4.position.x=6*12;
	  CubeBanDef4.position.y=0;
	  CubeBanDef4.position.z=6*2;
	  scene.add(CubeBanDef4);
	 // movePiece();
	 
	 var HeroToInitial= new TWEEN.Tween(CubeHero.position)
			.to( { y: 0, x:6*9, z:6*6}, 3000 ).start();
	 
	 var BanDef1ToInitial= new TWEEN.Tween(CubeBanDef1.position)
		.to( { y: 0,x: (6*8), z:(6*3)}, 9000 ).start();
	 
	 var BanDef2ToInitial= new TWEEN.Tween(CubeBanDef2.position)
		.to( { y: 0,x: (6*6), z:(6*3)}, 4000 ).start();
	 
	 var BanDef3ToInitial= new TWEEN.Tween(CubeBanDef3.position)
		.to( { y: 0,x: (6*11), z:(6*3)}, 9000 ).start();
		
	var BanDef4ToInitial= new TWEEN.Tween(CubeBanDef4.position)
		.to( { y: 0,x: (6*13), z:(6*3)}, 4000 ).start();
	  
	 */
	//trials

	
	// Create 10 objects to tween.
	//for(var i=0; i < 10; i++) {
	
	// Create a mesh and add to three.js scene
	//var mesh2 = new THREE.Mesh(new THREE.CubeGeometry(squareSize, squareSize, 40,0));
	//mesh2.position.x=6.25;
	//mesh2.position.y=20;//keep as -0.2
	//mesh2.position.z=6.25;
	//scene.add( mesh2 );
	
	 //load terrain	 
	  loader2.load("models/terrain1.js",function(geometry,materials){
	  var material2= new THREE.MeshLambertMaterial(materials);
	  mesh2 = new THREE.Mesh(geometry, new THREE.MeshFaceMaterial(materials) );	  
	  mesh2.position.x=0;
	  mesh2.position.y=-2;
	  mesh2.position.z=180;
	  mesh2.receiveShadow= true;
	  mesh2.scale.x=10;
	  mesh2.scale.y=10;
	  mesh2.scale.z=10;
	  scene.add(mesh2);
	  } );
	  scene.add(new THREE.AxisHelper(200));
	
      // Add OrbitControls so that we can pan around with the mouse.
      controls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
	// limitations
		controls.minPolarAngle = -10;//keepas 0
		controls.maxPolarAngle = 80 * Math.PI/180;
		controls.minDistance   = 10;
		controls.maxDistance   = 1500;// around 500
		controls.userZoomSpeed = 1.0;
        //add controls.update(); after renderer.render(scene,camera);



        //[jam] the main problem was in setTimeout(), as the number was being passed as 1 all the time, so only one piece was being moved
        //see this for more details: http://stackoverflow.com/questions/5226285/settimeout-in-a-for-loop-and-pass-i-as-value
		function applymove(piece,moves,index)
		{
		    console.log(index);
		        //xdocument.getElementById("test").innerHTML = moves;
		        updateBoard(piece, parseInt(moves[index][1]), parseInt(moves[index][2]), parseInt(moves[index][3]), parseInt(moves[index][4]));

		}

        //source: http://stackoverflow.com/questions/899102/how-do-i-store-javascript-functions-in-a-queue-for-them-to-be-executed-eventuall
		var wrapfunction = function (fn, context, params) {
		    return function () {
		        fn.apply(context, params);
		    };
		}
		var fun;
        //this is original
		for (s = 0; s < log2.length; s++) {

		    number = s;			//for some weird reason, i need to store the for loop counter in another variable to use it.
		    //function next_move() 
		    //{
		    x = (number + 1) * 4000;
		    h = moves[number].length;

		    if (h == 5) {

		        //document.getElementById("test").innerHTML = parseInt("3")+parseInt("3");
		        if (moves[number][0] == 'k') {

		            fun = wrapfunction(applymove, this, [k, moves, number]);
		            callbacks.push(fun);

		        }

		        if (moves[number][0] == 'd') {

		            fun = wrapfunction(applymove, this, [d, moves, number]);
		            callbacks.push(fun);

		        }

		        if (moves[number][0] == 'b') {
                    
		            fun = wrapfunction(applymove, this, [b, moves, number]);
		            callbacks.push(fun);

		        }

		    }
		}
	}
	
    // Renders the scene and updates the render as needed.
    function animate() {	  
      requestAnimationFrame(animate);
      //TWEEN.update();
      render();
      controls.update();	  
    }
	
	function render() {
	// Render our three.js scene and camera
	  renderer.render( scene, camera );
	}


	function play()
	{
	    timeout = setInterval(function () {

	        (callbacks.shift())();
	        if (callbacks.length == 0)
	        {
	            clearInterval(timeout);
	        }

	    }, 1500);



	}
	function nextmove()
	{
	    if (callbacks.length > 0) {
	        (callbacks.shift())();
	    }

	}

	function pause()
	{
	    clearInterval(timeout);
	}