using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Drill23ReferenceVsValue
{
    class Student
    {
        public int id { get; private set; }
        public string name { get; private set; }

        static void Main(string[] args)
        {
            Student s = new Student(); //this is a reference type
            s.id = 5; //this is a value type
            s.name = "Bob";
            Change(s);
            Console.WriteLine(s.id);
            Console.WriteLine(s.name);
        }
        static void Change(Student s)
        {
            s.id = 10; 
            s.name = "Frank";
        }
    }
}
