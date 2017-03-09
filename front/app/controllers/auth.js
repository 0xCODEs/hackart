import Ember from 'ember';

export default Ember.Controller.extend({
	isauthenticated: false,

	session: {
		'isauthenticated': false,
		'username': null,
		'email': null,
		'team': null,
		'isAdmin': false,
	},

	authenticate: function(username, password){
		console.log('username:', username);
		console.log('password:', password);

		Ember.$.ajax({
			type: "POST",
			url: "http://gitlab.nullify.online:8592/api/session/",
			data: { username: username, password: password }
		}).then((results) => {
			console.log('results', results);
			if (results.data.isauthenticated === true) {
				this.session.isauthenticated = true;
				console.log('auth succeeds');
			} else {
				console.log('auth fails');
			}
		});
	}
});
