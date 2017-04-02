using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//interface implementation
namespace Drill23b
{
    public interface IInterfaceTest
    {
        double getStuff();
        void somethingToDo();
    }
    public class ImplementationTest : IInterfaceTest
    {
        private string testCode;
        private double testNum;
        public ImplementationTest()
        {
            testCode = " ";
            testNum = 0.0;
        }
        public ImplementationTest(string s, double d)
        {
            testCode = s;
            testNum = d;
        }
        public double getStuff()
        {
            return testNum;
        }
        public void somethingToDo()
        {
            Console.WriteLine("Testing string: {0}", testCode);
            Console.WriteLine("Testing integer: {0}", testNum);
        }
    }
    class TestingInter
    {
        static void Test(string[] args)
        {
            ImplementationTest t1 = new ImplementationTest("First",100.0);
            ImplementationTest t2 = new ImplementationTest("Second",20000.0);
            t1.somethingToDo();
            t2.somethingToDo();
            Console.ReadKey();
        }
    }
}
