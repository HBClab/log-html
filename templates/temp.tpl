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
                margin-left: auto;
                margin-right: auto;
                table-layout: fixed;
                width: 100%;
            }
            table th:hover{
                background: greenyellow;
                cursor: pointer;
            }
            .bigcol {
                width: 40%;
            }
            .smallcol {
                width: 20%;
            }
            td {
                text-align: center;
                vertical-align: middle;
                border: 1px solid black;
            }
            .arrow-down:after {
                content: "";
                display: inline-block;
                vertical-align: middle;
                width: 0;
                height: 0;
                border-left: 10px solid transparent;
                border-right: 10px solid transparent;
                border-top: 10px solid black;
            }
        </style>
        <title>Accelerometer Files to BIDS Format Status</title>
    </head>
    <body>
    <table class="tbl">
        <tr>
            <th class="txt arrow-down bigcol">File </th>
            <th class="txt arrow-down smallcol">Status </th>
            <th class="txt arrow-down smallcol">Date </th>
            <th class="txt arrow-down smallcol">Time </th>
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
    <script>
    const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;

    const comparer = (idx, asc) => (a, b) => ((v1, v2) => 
        v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
        )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

    // do the work...
    document.querySelectorAll('th').forEach(th => th.addEventListener('click', (() => {
        const table = th.closest('table');
        Array.from(table.querySelectorAll('tr:nth-child(n+2)'))
            .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
            .forEach(tr => table.appendChild(tr) );
    })));
    </script>
    </body>
</html>