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
                // This block handles only FileNotFoundException
                catch (FileNotFoundException fileNotFoundException)
                {
                    Console.WriteLine("Please check if \"{0}\" is available", fileNotFoundException.FileName);
                }
                // Parent catch block for anything else, useful to catch any exception 
                catch (Exception exception)
                {
                    Console.WriteLine(exception.Message);
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
