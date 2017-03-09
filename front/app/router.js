import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('admin');
  this.route('challenge');
  this.route('login');
  this.route('catch-all');
  this.route('404');
  this.route('scoreboard');
});

export default Router;
