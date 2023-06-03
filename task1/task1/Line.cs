using System.Runtime.CompilerServices;

namespace task1
{
    public struct Line
    {
        const int maxValue = 90;
        const int minValue = -90;
        public double A { get; set; }

       public  double B { get; set; }

        double angleInDegrees;
        public double Angle
        {
            get => angleInDegrees;
            set
            {
                if (value < minValue || value > maxValue)
                    throw new ArgumentException("Значение должно быть от -90 до 90");
            }
        }

        public double AngleInDegrees
        {
            get =>  angleInDegrees;
        }

        public Line (double angleInDegrees, double a, double b) : this()
        {
            Angle= angleInDegrees;
            A = a;
            B = b;
        }

        public override string ToString() => $"y = {A}x + ({B})\"";

        public override bool Equals(object obj)
        {
            if (obj is Line)
                return AngleInDegrees == ((Line)obj).AngleInDegrees;

            throw new ArgumentException("Объект для сравнения не является углом");
        }

        public override int GetHashCode() => AngleInDegrees.GetHashCode();

        public static bool operator ==(Line x, Line y) => x.Equals(y);
        public static bool operator !=(Line x, Line y) => !x.Equals(y);



    }
}