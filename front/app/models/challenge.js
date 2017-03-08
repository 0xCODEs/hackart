import DS from 'ember-data';

export default DS.Model.extend({
    title: DS.attr('string'),
    points: DS.attr('number'),
    description: DS.attr('string'),
    flag: DS.attr('string'),   // why are we bringing in the flag, shouldn't we run the check server side?
    created: DS.attr('string')
});
