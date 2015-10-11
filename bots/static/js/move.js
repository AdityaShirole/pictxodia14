function movePiece() {
	var piece= new TWEEN.Tween(meshCube.position)
			.to( { y: 0, x:6.25*6, z:6.25*6}, 4000 );
	 //var tweenSand= new TWEEN.Tween(mesh2.position)
	//		.to( { y: 0,x: (6.25*10), z:(6.25*10)}, 3000 );
	  //tweenSly.chain(tweenSand);
	 piece.chain(tweenSly);

}