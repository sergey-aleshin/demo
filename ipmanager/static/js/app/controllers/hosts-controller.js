IPManager.controller('HostController', function ($scope, HostService, hosts) {
    var failureHandler = function (status) {
        $scope.hosts = HostService.list();
    }

    $scope.hosts = hosts;

    $scope.updateItem = function(item) {
        HostService.update(item).then(function (data) {}, failureHandler);
    };
});