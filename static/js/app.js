var gae_hopster_auth_frontend_module = angular.module('gae_hopster_auth_frontend',[]);

function init() {
      window.init();
    }

gae_hopster_auth_frontend_module.controller('mainController', function($scope, $window){
    var ROOT = 'https://gae-hopster-auth.appspot.com/_ah/api/';
    $window.init= function() {
        $scope.signin(true, $scope.userAuthed);
        var apisToLoad;
        var callback = function() {
            if (--apisToLoad == 0) {
              $scope.signin(true,
                  $scope.userAuthed);
            }
          }

        apisToLoad = 1; // must match number of calls to gapi.client.load()
        gapi.client.load('readWriteApi', 'v1', callback, ROOT);

     };

    $scope.signin = function(mode, authorizeCallback) {
        gapi.auth.authorize({
            client_id: '70641680892-nkjkmbqbd9cmilcrg9sg7pbc6a9gch1a.apps.googleusercontent.com',
            scope: 'https://www.googleapis.com/auth/userinfo.email',
            immediate: mode},
        authorizeCallback);
}
    $scope.userAuthed = function() {
        if (typeof gapi.client.oauth2 !== 'undefined')
        {
            request =
                gapi.client.oauth2.userinfo.get().execute(function (resp) {
                    if (!resp.code) {
                        // User is signed in, call my Endpoint
                    }
                });
        }

    }

    $scope.read = function() {
        if (typeof $scope.read_string_value == 'undefined' || $scope.read_string_value === '') {
                $window.alert('insert value for string value');
            }
        var ROOT = 'https://gae-hopster-auth.appspot.com/_ah/api/';
        message = {
                "string_value": $scope.read_string_value
            };
        gapi.client.readWriteApi.read(message).execute(function (resp) {
            if (typeof resp.id_value === 'undefined')
                $window.alert('error on read, message: ' + resp.error.message)
            else
                $window.alert('successful read, id: ' + resp.id_value);
        });
    }

    $scope.write = function() {
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

    }
});