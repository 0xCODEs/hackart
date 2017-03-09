import DS from 'ember-data';

export default DS.Model.extend({
	// profile: DS.belongsTo('profile'),
	username: DS.attr('string'),
	email: DS.attr('string'),
	password: DS.attr('string'),
	is_staff: DS.attr('string'),
});
