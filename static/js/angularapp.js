    var app = angular.module('App', []);
    app.controller('AppController', function($scope, $http) {


        $scope.sendValue=function(){

            $http.post('/sendHSV', $scope.hsvModel).then(function(response){
                console.log('response: ',response.data)
                $scope.inputImageSrc="data:image/jpeg;base64,"+response.data
            }, function(error){
                console.log('error : ')
            });
        }



        $scope. hsvModel={
                  "lh": 7656,
                  "ls": 7656,
                  "lv": 7656,
                  "uh": 7656,
                  "us": 7656,
                  "uv": 7656
        }

         $scope.inputImageSrc = "";

        $scope.$on("fileProgress", function(e, progress) {
          $scope.progress = progress.loaded / progress.total;
        });

    });
