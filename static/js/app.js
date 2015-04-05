var gae_hopster_auth_frontend = angular.module('gae_hopster_auth_frontend',[]);

gae_hopster_auth_frontend.controller('mainController', function($scope, $http){
    $scope.read= function() {
        message = {
            "id_value": $scope.id_value
        };
    }
    gapi.client.guestbook.messages.read_value(message).execute(function(resp){
        $scope.read_output = 'read successfull';
    });
});
