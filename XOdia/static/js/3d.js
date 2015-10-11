 // Set up the scene, camera, and renderer as global variables.
    var scene, camera, renderer;
	
	//variables for coordinates and createPiece function
	var xc, zc,piece, d="Dragon" , f= "fox";
	
	//Set squareSize as global variable. YO!
	var squareSize=6.25;
    init();
    animate();

    // Sets up the scene.
    function init() {

      // Create the scene and set the scene size.
      scene = new THREE.Scene();
      var WIDTH = window.innerWidth,
          HEIGHT = window.innerHeight;

      // Create a renderer and add it to the DOM.
      renderer = new THREE.WebGLRenderer({antialias:true});
      renderer.setSize(WIDTH, HEIGHT);
      document.body.appendChild(renderer.domElement);

      // Create a camera, zoom it out from the model a bit, and add it to the scene.
      camera = new THREE.PerspectiveCamera(45, WIDTH / HEIGHT, 0.1, 20000);
      camera.position.set(170,90,170);
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
      renderer.setClearColorHex(0x333F47, 1);

      // Create a light, set its position, and add it to the scene.
      var light = new THREE.DirectionalLight(0xffffff,2);
      light.position.set(0,30,0).normalize;
      scene.add(light);

	 
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
				if( ( (row==0) || (row==17) )&& ( (col==8) ||(col==9) ) )
				{	height=20;
					squareMaterial=material_black;
				}
				
				else
				{	height=0.0001;
					squareMaterial=material2;
					}
					
			
				
		        var square = new THREE.Mesh(new THREE.CubeGeometry(squareSize, squareSize, height,0));//add material after 1,1
		 
		        square.position.x = col * squareSize + squareSize / 2;
		        square.position.z = row * squareSize + squareSize / 2;
		        square.position.y = -0.01;
				
		 
		        square.rotation.x = -90 * Math.PI / 180;
		 
		        scene.add(square);
		    }
		}
	  
	 /* 
	 function draw() {
		 var loader2=new THREE.JSONLoader();
	  loader2.load("models/Dragon.js",function(geometry,materials){
	  var material2= new THREE.MeshLambertMaterial(materials);
	  mesh2 = new THREE.Mesh(geometry, new THREE.MeshFaceMaterial(materials) );
	  
	  
	  mesh2.position.x=(squareSize*6);
	  mesh2.position.y=0;
	  mesh2.position.z=(squareSize*6);
	  mesh2.castShadow= true;
	  
	   mesh2.scale.y=1;
	   mesh2.scale.x=1;
	   mesh2.scale.z=1;
	  scene.add(mesh2);
	  } );
		
		}
		
	draw();
	*/
	
	  var loader2=new THREE.JSONLoader();
	  loader2.load("models/board.js",function(geometry,materials){
	  var material2= new THREE.MeshLambertMaterial(materials);
	  mesh2 = new THREE.Mesh(geometry, new THREE.MeshFaceMaterial(materials) );  
	  mesh2.position.x=56.25;
	  mesh2.position.y=-0.2;
	  mesh2.position.z=56.25;
	  mesh2.acceptShadow= true;
	  mesh2.scale.x=50;
	  mesh2.scale.y=50;
	  mesh2.scale.z=50;
	  scene.add(mesh2);
	  } );
	  
	  //createPiece function call
	  createPiece(d,12,14);
	  createPiece(d,0,1);
	  createPiece(d,8,8);
	  createPiece(f,12,8);
	  
	  	  var loader2=new THREE.JSONLoader();
	  loader2.load("models/terrain.js",function(geometry,materials){
	  var material2= new THREE.MeshLambertMaterial(materials);
	  mesh2 = new THREE.Mesh(geometry, new THREE.MeshFaceMaterial(materials) );	  
	  mesh2.position.x=0;
	  mesh2.position.y=-1;
	  mesh2.position.z=180;
	  mesh2.acceptShadow= true;
	  mesh2.scale.x=10;
	  mesh2.scale.y=10;
	  mesh2.scale.z=10;
	  scene.add(mesh2);
	  } );
	  scene.add(new THREE.AxisHelper(200));
	  
	  
//mesh.castShadow = true;
      // Add OrbitControls so that we can pan around with the mouse.
      controls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
	// limitations
		controls.minPolarAngle = 0;
		controls.maxPolarAngle = 80 * Math.PI/180;
		controls.minDistance   = 10;
		controls.maxDistance   = 500;
		controls.userZoomSpeed = 1.0;
		//add controls.update(); after renderer.render(scene,camera);
    }
	
    // Renders the scene and updates the render as needed.
    function animate() {
      requestAnimationFrame(animate);
      
      // Render the scene.
      renderer.render(scene, camera);
      controls.update();
    }