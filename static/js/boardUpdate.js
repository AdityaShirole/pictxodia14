function uuuupdateBoard(piece, rows, cols,finalx,finaly) {//keep as single u later
	for(count=1; count<21 ; count++)
	{	
		if( ( (meshPiece[count].position.x)==rows) )
		{
			if( (meshPiece[count].position.z)==cols)
			{
				setTimeout(function()
							{scene.remove(meshPiece[count]);
 							 createPiece(count,piece,finalx,finaly );
								animate();}
								,5000);
			}
			
		}
	}
}
