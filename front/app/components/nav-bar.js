import Ember from 'ember';

export default Ember.Component.extend({
	auth: Ember.inject.service('authentication'),

	actions: {
		logout() {
			this.get('auth').logout();
		}
	}
});
