function setupTween() {
	
	
	
	TWEEN.removeAll();
	
	var easing = TWEEN.Easing.Elastic.InOut;
	
	var tweenHead = new TWEEN.Tween(current)
			.to( (6.25*14), 3000)
			.delay(1000)
			.easing(easing)
			.onUpdate( function() {
					mesh3.position.x= 20.35;
				} ).start();
	
	
	
	
}
		