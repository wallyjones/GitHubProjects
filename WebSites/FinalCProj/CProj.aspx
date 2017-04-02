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
        <p>New Item: <input data-bind="text: list" /></p>
        <p>A new thing!: <span data-bind="text: list"></span></p>
    </div>

    <script id="listMaker" type="text/html">
        <ul data-bind="foreach: koArray">
            <li>
                <input data-bind="text: list" />

            </li>
           
        </ul>
    </script>

    <button data-bind="click: addThing">Add stuff!</button>
    <button data-bind="click: removeThing">Remove stuff!</button>


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
        function viewModel() {
            var self = this;
            self.koArray = ko.observableArray([
                { list: '' }
            ]);
            self.addThing = function () {
                self.koArray.push({ list: "New thing... " + new Date() });
            };
            self.removeThing = function () {
                self.koArray.pop(this);
            }
        }
        ko.applyBindings(new viewModel());
    </script>

</body>
</html>
