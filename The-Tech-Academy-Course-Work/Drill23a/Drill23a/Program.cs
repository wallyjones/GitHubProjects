using System;


namespace Overloading
{
    public class Vehicle
    {
        public void attributes(int id)
        { }
        public void attributes(string name)
        { }
    }
}

namespace Overriding
{
    public class Parent
    {
        public virtual void Genetics()
        { }
    }
    public class Child : Parent
    {
        public override void Genetics()
        { }
    }
}

namespace Derived
{
    public class Shape
    {
        public void setWidth(int w)
        {
            width = w;
        }
        public void setHeight(int h)
        {
            height = h;
        }
        protected int width;
        protected int height;
    }

    // Derived class
    class Rectangle : Shape
    {
        public int getArea()
        {
            return (width * height);
        }
    }
}

//sealed class
namespace Sealed
{
    public sealed class Shape
        //this will not work because of the sealed access modifier here
        //sealed classes are not inheritable but can inherit
    {
        public void setWidth(int w)
        {
            width = w;
        }
        public void setHeight(int h)
        {
            height = h;
        }
        protected int width;
        protected int height;
    }
    class Rectangle : Shape
    {
        public int getArea()
        {
            return (width * height);
        }
    }
}