import Ember from 'ember';

export default Ember.Controller.extend({
	flag: '',
	actions: {
		popModal(challenge) {
			const modal = document.getElementById(`modal-${challenge.id}`);
			modal.style.display = 'block';
			console.log('gets to popModal', challenge);
		},
		closeModal(challenge) {
			const modal = document.getElementById(`modal-${challenge.id}`);
			modal.style.display = 'none';
			console.log('gets to closeModal', challenge);
		},
		submitFlag(id) {

			console.log('challenge', id);
			const flag = this.get('flag');

			Ember.$.ajax({
				type: "POST",
				url: `http://gitlab.nullify.online:8592/api/flags/${id}/`,
				data: { flag: flag },
				xhrFields: {
				    withCredentials: true
				},
				crossDomain: true
			}).then((results) => {
				console.log('results', results);
			});

		}
	}
});
