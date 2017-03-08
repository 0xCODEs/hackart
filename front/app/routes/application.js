import Ember from 'ember';

export default Ember.Route.extend({
	beforeModel: function (transition) {
		this.authCheck(transition);

		// if (transition.targetName === 'login') {
		// 	this.transitionTo('challenge');
		// }
	},

	authCheck: function(transition) {
		const t = this;
		const auth = t.controllerFor('auth');

		if(!auth.session.isauthenticated && transition.targetName !== 'login'){
			transition.abort();
			t.transitionTo('login');
		}
	},

	setupController: function (controller) { 
		controller.set('authController', this.controllerFor('auth'));
	},

	actions: {
		willTransition: function(transition) {
			this.authCheck(transition);
		}
	}
});
