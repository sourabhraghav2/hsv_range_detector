var app = angular.module('App');

 app.directive('slider', function() {
        return {
            restrict: 'E',
            scope: { properties: '=',model: '='  },
            templateUrl: 'static/htmlTemplates/slider.html',
            controller:function($scope){
                $scope.testMe=function(){
                    alert ("Hiiiiiii");
                }
            }
        };
    });


app.directive("ngFileSelect", function(fileReader, $timeout,$http) {
    return {
      scope: {
        ngModel: '='
      },
      link: function($scope, el) {
        function getFile(file) {
          fileReader.readAsDataUrl(file, $scope)
            .then(function(result) {
              $timeout(function() {
                var inputImage=result.split(',')
                $http.post('/inputImage',{'inputImage':inputImage[1]} ).then(function(response){
                    console.log('response: ',response.data)
                    console.log('Image : ',result)
                    if(response.data=='Uploaded'){
                        $scope.ngModel = result;
                    }else{
                        console.log('Back end issue')
                    }
                }, function(error){
                    console.log('error : ')
                });


              });
            });
        }

        el.bind("change", function(e) {
          var file = (e.srcElement || e.target).files[0];
          getFile(file);
        });
      }
    };
  });