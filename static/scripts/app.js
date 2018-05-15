'use strict';

var theApp = angular.module('theApp', [
    'ngRoute', 'ngMaterial'
])

theApp.config(function ($routeProvider) {
  $routeProvider
    .when('/coolstuff', {
      templateUrl: '/app-trial/static/pages/coolstuff.html',
      controller: 'coolStuff'
    })
    .otherwise({
      redirectTo: '/coolstuff'
    });
})

theApp.service('mathService', function() {
  this.add = function(a) { return a + 1 };
});

theApp.controller('coolStuff', function ($scope, mathService) {
  $scope.doSquare = function() {
    $scope.answer = mathService.add($scope.number);
  } 
})