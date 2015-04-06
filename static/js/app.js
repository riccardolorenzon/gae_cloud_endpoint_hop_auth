var gae_hopster_auth_frontend_module = angular.module('gae_hopster_auth_frontend',[]);

function init() {
      window.init();
    }

gae_hopster_auth_frontend_module.controller('mainController', function($scope, $window){
    $window.init= function() {
      $scope.$apply($scope.load_readwrite_gae);
    };

    $scope.load_readwrite_gae = function() {
        var ROOT = 'https://gae-hopster-auth.appspot.com/_ah/api/';
        gapi.client.load('readWriteApi', 'v1', function() {
            // TODO insert initialization values
        }, ROOT);
    };

    $scope.read = function() {
        var ROOT = 'https://gae-hopster-auth.appspot.com/_ah/api/';
        gapi.client.load('readWriteApi', 'v1', function() {
            if (typeof $scope.read_string_value == 'undefined' || $scope.read_string_value === '')
            {
                $window.alert('insert value for string value');
            }
            message = {
                "string_value": $scope.read_string_value
            };
            gapi.client.readWriteApi.read(message).execute(function (resp) {
                if (typeof resp.id_value === 'undefined')
                    $window.alert('error on read, message: ' + resp.error.message)
                else
                    $window.alert('successful read, id: ' + resp.id_value);
            });
        }, ROOT);
    }

    $scope.write = function() {
        var ROOT = 'https://gae-hopster-auth.appspot.com/_ah/api/';
        gapi.client.load('readWriteApi', 'v1', function() {
            if (typeof $scope.write_string_value == 'undefined' || $scope.write_string_value === '')
            {
                $window.alert('insert value for string value');
            }
            message = {
                "string_value": $scope.write_string_value
            };
            gapi.client.readWriteApi.write(message).execute(function (resp) {
                if (typeof resp.id_value === 'undefined')
                    $window.alert('error on write, message: ' + resp.error.message)
                else
                    $window.alert('successful write, id: ' + resp.id_value);
            });
        }, ROOT);

    }
});