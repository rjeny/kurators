const fullGroup = 20;

function calculateAvg($obj) {
    let sum = 0;
    let smart_sum = 0;
    let groupCounter = parseInt($('#id_students_count').val());
    let avgStr = '';

    let $list = $obj.parent();
    $list.find('input').each(function (i) {
        let value = parseInt($(this).val());

        if (!value) {
            value = 0;
        }

        avgStr += value + ',';
        sum += value;

        switch (value) {
            case 10:
                smart_sum += 9.5;
                break;
            case 4:
                smart_sum += 5;
                break;
            case 3:
                smart_sum += 4.5;
                break;
            case 2:
                smart_sum += 3.5;
                break;
            case 1:
                smart_sum += 2;
                break;
            default:
                smart_sum += value;
        }
    });

    console.log(sum / groupCounter);
    console.log(smart_sum / groupCounter);
    avgStr = avgStr.slice(0, -1);
}

$('#id_students_count').on('input', function () {
    let $place = $('#students-qual-group');
    let $place2 = $('#students-qual-in-group');
    $place.html('');
    $place2.html('');
    let value = $(this).val();
    for (let i = 0; i < value; i++) {
        $place.append('<input name="students-qual-in-' + i + '" class="students-qual-object" data-index="' + i + '" />');
        $place2.append('<input name="students-qual-in-' + i + '" class="students-qual-object" data-index="' + i + '" />');
    }
    $place.append('<a class="clear-block">очистить</a>');
    $place2.append('<a class="clear-block">очистить</a>');
});

$('#students-qual-group, #students-qual-in-group').on('input', '.students-qual-object', function () {
    let $this = $(this);
    $this.removeClass('is-invalid');
    let value = parseInt($this.val());
    if (value >= 2 && value <= 10) {
        $this.attr({'prev-value': value});
        let index = parseInt($this.attr('data-index'));
        $this.parent().find('input.students-qual-object[data-index="' + (index + 1) + '"]').focus();
    }
    if (value < 0 || value > 10) {
        $this.val($this.attr('prev-value'));
        $this.addClass('is-invalid');
    }

    calculateAvg($this);
});