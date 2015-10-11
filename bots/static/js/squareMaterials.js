var material_black = new THREE.MeshLambertMaterial( { ambient: 0x000000, color: 0x000000 } ); //color: object hexadecimal color after the 0x
var material2 = new THREE.MeshLambertMaterial( { ambient: 0x333f47, color: 0x33f47 } ); //color: object hexadecimal color after the 0x
		
		var height=0.001;
		var squareSize=6.25;
for(var row=0;row<18;row+=17)
{
	for(var col=0;col<8;col++)
		{ 
			squareMaterial=material_black;
			 var square = new THREE.Mesh(new THREE.CubeGeometry(squareSize, squareSize, height,0),squareMaterial);//add material after 1,1
		 
		        square.position.x = col * squareSize + squareSize / 2;
		        square.position.z = row * squareSize + squareSize / 2;
		        square.position.y = -0.01;
				
		 
		        square.rotation.x = -90 * Math.PI / 180;
				square.receiveShadow=true;
		        scene.add(square);
		}
		/*
	for(col=9;col<18;col++)
		{
			squareMaterial=material_black;
			 var square = new THREE.Mesh(new THREE.CubeGeometry(squareSize, squareSize, height,0),squareMaterial);//add material after 1,1
		 
		        square.position.x = col * squareSize + squareSize / 2;
		        square.position.z = row * squareSize + squareSize / 2;
		        square.position.y = -0.01;
				
		 
		        square.rotation.x = -90 * Math.PI / 180;
				square.receiveShadow=true;
		        scene.add(square);
		}*/
}
			