from quart import Quart, request, abort, render_template_string
import time
import asyncio
app = Quart(__name__)


@app.route('/')
async def hello_world():  # put application's code here
    return await render_template_string('''
    <html>
    <head><title>Web DOS?</title></head>
    <body>
        <div class="content">
            <h1 class="main_content_text">
                Hello<br>
                &nbsp; &nbsp; &nbsp; &nbsp; Bro
            </h1>
             <h2 class="main_content">
                You can hack this site? 
            </h2>    
        </div>
        <script>
        //window.onload = function() {
        //    var request = new Request('/await?timeout=1');
        //    fetch(request).then(function(response) {
        //        return response.text();
        //        }).then(function(text) {
        //    console.log(text);
        //    });
        //};
        console.log('');
        </script>
    </body>
    </html>    
    ''')
async def sleep(timeout):
    return await asyncio.sleep(timeout)
@app.route('/await')
async def await_func():
    timeout = float(request.args.get('timeout'))
    if timeout <= 100:
        await sleep(timeout)
        return 'OK, wait is successful'
    else:
        return abort(403)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
