<!DOCTYPE html>
<html>
    <head>
        <style>
            .txt {
                font-size: 40px;
            }
            .redtext {
	            color: red;
            }
            .greentext {
	            color: green;
            }
            .tbl{
                width: 600px;
                margin-left: auto;
                margin-right: auto;
            }
            td {
                text-align: center;
                vertical-align: middle;
                border: 1px solid black;
            }
        </style>
        <title>Accelerometer Files to BIDS Format Status</title>
    </head>
    <body>
    <table class="tbl">
        <tr>
            <th class="txt">File</th>
            <th class="txt">Status</th>
            <th class="txt">Date</th>
            <th class="txt">Time</th>
        </tr>
        {% for item in accel_files %}
            <tr>
                <td class="txt"><a href="{{item.path}}">{{item.filename}}</a></td>
                <td><span class="{{item.css}} txt">{{item.status}}</span></td>
                <td><span class="txt">{{item.date}}</span></td>
                <td><span class="txt">{{item.time}}</span></td>
            </tr>
        {% endfor %}
    </table>
    </body>
</html>