namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox5 = new System.Windows.Forms.TextBox();
            this.textBox6 = new System.Windows.Forms.TextBox();
            this.textBox8 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.textBox9 = new System.Windows.Forms.TextBox();
            this.label9 = new System.Windows.Forms.Label();
            this.btn_CreateAssem = new System.Windows.Forms.Button();
            this.txt_target = new System.Windows.Forms.TextBox();
            this.txt_PartName1 = new System.Windows.Forms.TextBox();
            this.txt_PartName2 = new System.Windows.Forms.TextBox();
            this.txt_PartName3 = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.txt_PartName4 = new System.Windows.Forms.TextBox();
            this.btn_target = new System.Windows.Forms.Button();
            this.label12 = new System.Windows.Forms.Label();
            this.txt_AssemName = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(551, 361);
            this.button1.Margin = new System.Windows.Forms.Padding(2);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(94, 51);
            this.button1.TabIndex = 0;
            this.button1.Text = "Расчет";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(11, 51);
            this.textBox1.Margin = new System.Windows.Forms.Padding(2);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(76, 20);
            this.textBox1.TabIndex = 1;
            // 
            // textBox5
            // 
            this.textBox5.Location = new System.Drawing.Point(11, 86);
            this.textBox5.Margin = new System.Windows.Forms.Padding(2);
            this.textBox5.Name = "textBox5";
            this.textBox5.Size = new System.Drawing.Size(76, 20);
            this.textBox5.TabIndex = 5;
            // 
            // textBox6
            // 
            this.textBox6.Location = new System.Drawing.Point(11, 120);
            this.textBox6.Margin = new System.Windows.Forms.Padding(2);
            this.textBox6.Name = "textBox6";
            this.textBox6.Size = new System.Drawing.Size(76, 20);
            this.textBox6.TabIndex = 6;
            // 
            // textBox8
            // 
            this.textBox8.Location = new System.Drawing.Point(11, 155);
            this.textBox8.Margin = new System.Windows.Forms.Padding(2);
            this.textBox8.Multiline = true;
            this.textBox8.Name = "textBox8";
            this.textBox8.Size = new System.Drawing.Size(668, 202);
            this.textBox8.TabIndex = 8;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Times New Roman", 13.824F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label1.Location = new System.Drawing.Point(11, 7);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(263, 25);
            this.label1.TabIndex = 9;
            this.label1.Text = "Введите входные данные";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(94, 54);
            this.label2.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(121, 13);
            this.label2.TabIndex = 10;
            this.label2.Text = "I - передаточное число";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(94, 93);
            this.label6.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(195, 13);
            this.label6.TabIndex = 14;
            this.label6.Text = "P - мощность электродвигателя, кВт";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(94, 127);
            this.label7.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(228, 13);
            this.label7.TabIndex = 15;
            this.label7.Text = "n - количество оборотов двигателя, об/мин";
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(327, 56);
            this.textBox2.Margin = new System.Windows.Forms.Padding(2);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(55, 20);
            this.textBox2.TabIndex = 2;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(394, 59);
            this.label3.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(213, 13);
            this.label3.TabIndex = 11;
            this.label3.Text = " N - число зубьев циклоидального диска";
            this.label3.Click += new System.EventHandler(this.Label3_Click);
            // 
            // textBox9
            // 
            this.textBox9.Location = new System.Drawing.Point(327, 86);
            this.textBox9.Margin = new System.Windows.Forms.Padding(2);
            this.textBox9.Multiline = true;
            this.textBox9.Name = "textBox9";
            this.textBox9.Size = new System.Drawing.Size(55, 19);
            this.textBox9.TabIndex = 18;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(394, 92);
            this.label9.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(104, 13);
            this.label9.TabIndex = 19;
            this.label9.Text = "e - Эксцентриситет";
            // 
            // btn_CreateAssem
            // 
            this.btn_CreateAssem.Location = new System.Drawing.Point(551, 417);
            this.btn_CreateAssem.Name = "btn_CreateAssem";
            this.btn_CreateAssem.Size = new System.Drawing.Size(128, 103);
            this.btn_CreateAssem.TabIndex = 30;
            this.btn_CreateAssem.Text = "Create Assembly";
            this.btn_CreateAssem.UseVisualStyleBackColor = true;
           
            // 
            // txt_target
            // 
            this.txt_target.Location = new System.Drawing.Point(91, 365);
            this.txt_target.Name = "txt_target";
            this.txt_target.Size = new System.Drawing.Size(347, 20);
            this.txt_target.TabIndex = 31;
            // 
            // txt_PartName1
            // 
            this.txt_PartName1.Location = new System.Drawing.Point(91, 391);
            this.txt_PartName1.Name = "txt_PartName1";
            this.txt_PartName1.Size = new System.Drawing.Size(183, 20);
            this.txt_PartName1.TabIndex = 32;
            this.txt_PartName1.Text = "Output shaft";
            // 
            // txt_PartName2
            // 
            this.txt_PartName2.Location = new System.Drawing.Point(91, 417);
            this.txt_PartName2.Name = "txt_PartName2";
            this.txt_PartName2.Size = new System.Drawing.Size(183, 20);
            this.txt_PartName2.TabIndex = 33;
            this.txt_PartName2.Text = "Housing ring";
            // 
            // txt_PartName3
            // 
            this.txt_PartName3.Location = new System.Drawing.Point(91, 443);
            this.txt_PartName3.Name = "txt_PartName3";
            this.txt_PartName3.Size = new System.Drawing.Size(183, 20);
            this.txt_PartName3.TabIndex = 34;
            this.txt_PartName3.Text = "Input shaft";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(8, 370);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(70, 13);
            this.label4.TabIndex = 35;
            this.label4.Text = "Target Folder";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(13, 398);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(67, 13);
            this.label5.TabIndex = 36;
            this.label5.Text = "Part-1 name ";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(13, 424);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(67, 13);
            this.label8.TabIndex = 37;
            this.label8.Text = "Part-2 name ";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(13, 450);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(67, 13);
            this.label10.TabIndex = 38;
            this.label10.Text = "Part-3 name ";
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(13, 476);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(67, 13);
            this.label11.TabIndex = 40;
            this.label11.Text = "Part-4 name ";
            // 
            // txt_PartName4
            // 
            this.txt_PartName4.Location = new System.Drawing.Point(91, 469);
            this.txt_PartName4.Name = "txt_PartName4";
            this.txt_PartName4.Size = new System.Drawing.Size(183, 20);
            this.txt_PartName4.TabIndex = 39;
            this.txt_PartName4.Text = "Satellite";
            // 
            // btn_target
            // 
            this.btn_target.Location = new System.Drawing.Point(444, 365);
            this.btn_target.Name = "btn_target";
            this.btn_target.Size = new System.Drawing.Size(75, 23);
            this.btn_target.TabIndex = 41;
            this.btn_target.Text = "...";
            this.btn_target.UseVisualStyleBackColor = true;
            this.btn_target.Click += new System.EventHandler(this.btn_target_Click);
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(13, 502);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(82, 13);
            this.label12.TabIndex = 43;
            this.label12.Text = "Assembly Name";
            // 
            // txt_AssemName
            // 
            this.txt_AssemName.Location = new System.Drawing.Point(101, 495);
            this.txt_AssemName.Name = "txt_AssemName";
            this.txt_AssemName.Size = new System.Drawing.Size(337, 20);
            this.txt_AssemName.TabIndex = 42;
            this.txt_AssemName.Text = "Test Assembly";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(761, 521);
            this.Controls.Add(this.label12);
            this.Controls.Add(this.txt_AssemName);
            this.Controls.Add(this.btn_target);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.txt_PartName4);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.txt_PartName3);
            this.Controls.Add(this.txt_PartName2);
            this.Controls.Add(this.txt_PartName1);
            this.Controls.Add(this.txt_target);
            this.Controls.Add(this.btn_CreateAssem);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.textBox9);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox8);
            this.Controls.Add(this.textBox6);
            this.Controls.Add(this.textBox5);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button1);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "Form1";
            this.Text = "Расчет привода";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox5;
        private System.Windows.Forms.TextBox textBox6;
        private System.Windows.Forms.TextBox textBox8;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox textBox9;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Button btn_CreateAssem;
        private System.Windows.Forms.TextBox txt_target;
        private System.Windows.Forms.TextBox txt_PartName1;
        private System.Windows.Forms.TextBox txt_PartName2;
        private System.Windows.Forms.TextBox txt_PartName3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.TextBox txt_PartName4;
        private System.Windows.Forms.Button btn_target;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.TextBox txt_AssemName;
    }
}

