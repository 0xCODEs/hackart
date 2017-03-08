import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('admin');
  this.route('challenges');
  this.route('login');
  this.route('catch-all');
  this.route('404');
});

export default Router;
