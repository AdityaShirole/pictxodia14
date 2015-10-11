
function  createPiece(piece,xc,zc) {

	var loader = new THREE.JSONLoader();
      loader.load( "models/"+ piece+".js", function(geometry,materials){
        var material = new THREE.MeshLambertMaterial(materials);
        mesh = new THREE.Mesh(geometry,new THREE.MeshFaceMaterial( materials) );
       
	   mesh.position.x=(squareSize*xc);
	  mesh.position.y=0;
	  mesh.position.z=(squareSize*zc);
	  mesh.scale.y=1;
	   mesh.scale.x=1;
	   mesh.scale.z=1;

		mesh.castShadow= true;
		
	  scene.add(mesh);
      });
	  
	  }
	
	