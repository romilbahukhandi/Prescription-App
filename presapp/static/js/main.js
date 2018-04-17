$(document).ready(function() {
    $('select').material_select();
    $('ul.tabs').tabs();
    $('.modal').modal();
    $(".dropdown-button").dropdown();
    $('input[type=radio][name=agechoice]').on('change', function() {
        if ($("#id_agechoice_0").prop("checked")) {
            $("#id_payear").attr('disabled', false);
        } else if ($("#id_agechoice_1").prop("checked")) {
            $("#id_payear").attr('disabled', true);
        }
    });
});
