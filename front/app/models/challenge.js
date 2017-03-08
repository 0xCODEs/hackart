import DS from 'ember-data';

export default DS.Model.extend({
    title: DS.attr('string'),
    points: DS.attr('number'),
    description: DS.attr('string'),
    flag: DS.attr('string'),
    created: DS.attr('string')
});
