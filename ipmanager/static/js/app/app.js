'use strict';

var IPManager = angular.module("IPManager", ["mk.editablespan", "ngCookies"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

IPManager.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

IPManager.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/main.html",
            controller: "HostController",
            resolve: {
                hosts: function (HostService) {
                    return HostService.list();
                }
            }
        })
        .otherwise({
            redirectTo: '/'
        })
});
