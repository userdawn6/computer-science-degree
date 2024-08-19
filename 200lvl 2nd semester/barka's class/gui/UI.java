import javax.swing.*;
import java.awt.*;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UI {
    JFrame window = new JFrame("Physics");
    JTextField tfMass = new JTextField("Enter Mass");
    JTextField tfAcceleration = new JTextField("Acceleration");
    JButton btnCalculate = new JButton("Calculate");

    void drawUI(){
        window.add(tfMass);
        window.add(tfAcceleration);
        window.add(btnCalculate);

        btnCalculate.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    physics physics = new physics();
                    float mass = Float.valueOf(tfMass.getText());
                    float acceleration = Float.valueOf(tfAcceleration.getText());

                    JOptionPane.showMessageDialog(null, physics.calculateForce(mass, acceleration));

                }catch(NumberFormatException nfe){
                    JOptionPane.showMessageDialog(null, "enter only numbers please");
                    nfe.printStackTrace();
                }catch (Exception E){
                    JOptionPane.showMessageDialog(null, "unexpected error");

                }
            }
        });

        window.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        window.setLayout(new GridLayout(3,1));
        window.setSize(200, 250);
        window.setVisible(true);
    }

}