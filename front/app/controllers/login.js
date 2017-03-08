import Ember from 'ember';

export default Ember.Controller.extend({
	authController: null,
	username: '',
	password: '',

	actions: {
		login() {
			const username = this.get('username');
			const password = this.get('password');
			const authController = this.get('authController');

			authController.authenticate(username, password);
		}
	}
});
