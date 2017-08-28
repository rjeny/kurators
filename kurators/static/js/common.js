function BSCommon() {
    this.runAlert = function(args) {
        let settings = {
            msg: 'Будьте осторожней!',
            header: 'Внимание!',
            type: 'warning',
            afterObject: true,
            selector: 'h1',
            timeout: 0
        };

        for (let arg in args) {
            if (args.hasOwnProperty(arg) && settings.hasOwnProperty(arg)) {
                settings[arg] = args[arg];
            } else {
                console.warn('Unexpected arg: ' + arg);
            }
        }

        $(settings.selector).after(
            `<div class="alert alert-${ settings.type } alert-dismissible fade show" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
            <strong>${ settings.header }</strong> ${ settings.msg }
            </div>`
        )

        if (settings.timeout) {
            setTimeout(function () {
                $('.alert').alert('close');
            }, settings.timeout);
        }
    }
}
