/**
 * Created by ab01 on 7/8/2017.
 */

function botton01() {

 $.ajax({
        url: "/get_scipt/",
        type: 'GET',
        data: {
          'par1': 'obana',
          'csrftoken': document.getElementsByName("csrfmiddlewaretoken")[0].value,
        },

        success: function (json) {
            alert('success');

            if (json) {
                console.dir(json);
            };

        }
    });

}