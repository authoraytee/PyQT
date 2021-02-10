
using Microsoft.SqlServer.Server;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        double i, Tnom, p, n, d2, d1, mod, b, R, Rr, N; //входные данные

        private void btn_target_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog target = new FolderBrowserDialog();
            target.ShowDialog();
            txt_target.Text = target.SelectedPath;
        }

       

      

       

        double dk, nvih, Tvh, Tvih, Koef, ex, z2, koeft, Fx, Fy, M, Fin, Fr, Pr, nk, Ctr;  // выходные данные

      

     
        

        public Form1()
        {
            InitializeComponent();
            button1.Click += Button1_Click;
          
        }

        private void Button1_Click(object sender, EventArgs e)
        {
           
          
           
            i = double.Parse(textBox1.Text);
            N = double.Parse(textBox2.Text); 
            p = double.Parse(textBox5.Text);
            n = double.Parse(textBox6.Text);
            mod = double.Parse(textBox9.Text);
                nvih = n / i;
                z2 = N + 1;
                Tvh = (30 * n) / (3.14 * n);
                Tvih =  (9950*p*0.849)/nvih;
                Koef = Math.Pow((N / (3.7 * (N + 4))), 1.0/4.0 );
                d1 = mod * N;
                d2 = mod * z2;
                ex = 0.5 * d2 * Koef / z2;
                koeft = 2 * ex * z2 / d2;
                Fx =(1.2 * koeft - 0.66 + (8 / Math.Pow(z2, 2.0))) * 1000 * n / (ex * N);
                Fy = -1000 * n / (ex * N);
                M = (7.8 * 0.000001 * 3.14 * d1 * d1 * 69)/16;
                dk = 3.14 * n / 30;
                Fin = M * Math.Pow(dk, 2.0) * ex * 0.001;
                Fr = Math.Pow((Math.Pow((Fx+Fin), 2.0))+ Math.Pow(Fy, 2.0), 1.0 / 2.0);
                Pr = 1.2 * Fr * 1.3 * 1;
                nk = n + nvih;
                Rr = koeft / ex;
                R = ex * N;
                Ctr = 0.8 * Pr * Math.Pow((60 * nk * 10000 / (1000000 * 1 * 0.55)), 0.3);
            textBox8.Text = "Частота вращения входного вала: " + Math.Round(nvih, 2).ToString() + " об/мин" +
            Environment.NewLine + "Крутящий момент на входном валу редуктора: " + Math.Round(Tvh, 2).ToString() + " Н*м" +
            Environment.NewLine + "Крутящий момент на выходном валу: " + Math.Round(Tvih, 2).ToString() + " Н*м" +
            Environment.NewLine + "Рассчитываем коэффициент укорочения эпициклоиды: " + Math.Round(Koef, 3).ToString() +
            Environment.NewLine + "Эксцентриситет передачи: " + Math.Round(ex, 2).ToString() +
            Environment.NewLine + "Уточненное значение коэффициента укорочения эпициклоиды: " + Math.Round(koeft, 3).ToString() +
            Environment.NewLine + "Сумма проекций всех сил в зацеплении зубьев сателлита на ось X: " + Math.Round(Fx, 2).ToString() + " Н" +
            Environment.NewLine + "Cумму проекций сил в зацеплении зубьев сателлита на ось Y : " + Math.Round(Fy, 2).ToString() + " Н" +
            Environment.NewLine + "Ориентировочная масса сателлита  : " + Math.Round(M, 2).ToString() + " кг" +
            Environment.NewLine + "Сила энерции действующая на сателлит  : " + Math.Round(Fin, 2).ToString() + " Н" +
            Environment.NewLine + "Радиальная сила подшипника сателлита по формуле  : " + Math.Round(Fr, 2).ToString() + " Н" +
            Environment.NewLine + "Эквивалентная динамическая нагрузка подшипника  : " + Math.Round(Pr, 2).ToString() + " Н" +
            Environment.NewLine + "Относительная частота вращения колец подшипника  : " + Math.Round(nk, 2).ToString() + " об/мин" +
            Environment.NewLine + "Требуемая динамическая грузоподъемность радиального роликового подшипника : " + Math.Round(Ctr, 2).ToString() + " Н" +
            Environment.NewLine + "Радиус сателлита : " + Math.Round(R, 2).ToString() + " мм" +
            Environment.NewLine + "Радиус цевки : " + Math.Round(Rr, 2).ToString() + " мм";
        }

        private void Label3_Click(object sender, EventArgs e)
        {
           
        }
    }
}
