<%@ Page Language="C#" AutoEventWireup="true" CodeFile="CProj.aspx.cs" Inherits="CProj" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Welcome to Make-A-List</title>
    <link rel="stylesheet" href="StyleSheet.css" />
</head>

<body>
    <form id="form1" runat="server">
    <h1>Welcome to Make-A-List</h1>
    <h3>Where you can organize Bands, Shopping Lists, etc. On the fly! </h3>
    <div data-bind="template: 'listMaker'">
        <p>1: <input data-bind="text: koArray" /></p>
    </div>

    <script id="listMaker" type="text/html">
        <ul>
           {{each(index, list) koArray }}
                <li>${list.name}</li>
            {{/each}}
        </ul>
    </script>

    <button data-bind="click: addThing">Add stuff!</button>


    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />

    <footer>This SPA, Single Page Application, utilizes Knockout.js library</footer>
    </form>

    <script src="Scripts/knockout-3.4.2.js"></script>
    <script type="text/javascript">
        function list(name) {
            return {
                name: ko.observable(name)
            };
        }
        var viewModel = {
            koArray: ko.observableArray([new list]),
            addThing: function () {
                this.koArray.push(new list("More please!")
                    )
            }
        };
        ko.applyBindings(viewModel);
    </script>

</body>
</html>
