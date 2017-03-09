import Ember from 'ember';

export default Ember.Controller.extend({
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
		}
	}
});
