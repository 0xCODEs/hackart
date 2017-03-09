import Ember from 'ember';

export default Ember.Component.extend({
	auth: Ember.inject.service('authentication'),

	is_staff: Ember.computed(() => {
		return this.get('auth').user.is_staff;
	}),

	actions: {
		logout() {
			this.get('auth').logout();
		}
	}
});
