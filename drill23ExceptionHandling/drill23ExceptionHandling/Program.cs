using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace drill23ExceptionHandling
{
    class ExceptionHandling
        {
            public static void Main()
            {
                StreamReader SR = null;
                try
                {
                    SR = new StreamReader("C:\\random.txt");
                    Console.WriteLine(SR.ReadToEnd()); //readtoend will display text from txt file
                }
                // Parent catch block for anything else, useful to catch any exception not just filenotfound.exception
                catch (Exception ex)
                {
                    string filePath = "C:\\Error.txt";
                // this hopefully creates an error.txt file for the exception that is caught.
                    using (StreamWriter SW = new StreamWriter(filePath, true))
                    {
                        SW.WriteLine("Message :" + ex.Message + "<br/>" + Environment.NewLine + "StackTrace :" + ex.StackTrace +
                        "" + Environment.NewLine + "Date :" + DateTime.Now.ToString());
                        SW.WriteLine(Environment.NewLine + "-----------------------------------------------------------------------------" + Environment.NewLine);
                    }
                }
                finally //Wraps up the program resources if empty
                {
                    if (SR != null)
                    {
                        SR.Close();
                    }
                }
            }
        }
}
