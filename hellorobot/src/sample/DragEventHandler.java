package sample;

import javafx.event.EventHandler;
import javafx.scene.Node;
import javafx.scene.input.MouseEvent;

public class DragEventHandler implements EventHandler<MouseEvent> {
    private Node group;
    private double mouseX;
    private double mouseY;

    public DragEventHandler(Node group) {
        this.group = group;
    }

    /**
     * Invoked when a specific event of the type for which this handler is
     * registered happens.
     *
     * @param event the event which occurred
     */
    @Override
    public void handle(MouseEvent event) {
        if (event.getEventType() == MouseEvent.MOUSE_PRESSED) {
           mouseX = event.getSceneX();
           mouseY = event.getSceneY();
           //System.out.println("Event: " + event.getX() + " " +event.getY() + " | " + mouseX + " " + mouseY);
           //System.out.println("Scene: " + event.getSceneX() + " " +event.getSceneY() + " | " + mouseX + " " + mouseY);
        }
        if (event.getEventType() == MouseEvent.MOUSE_DRAGGED) {
            // Help with dragging:
            // https://stackoverflow.com/questions/32680689/javafx-mouseevent-location-accuracy-degrades-over-time-results-in-node-movement
            double newMouseX = event.getSceneX();
            double newMouseY = event.getSceneY();
            double deltaX = newMouseX - mouseX;
            double deltaY = newMouseY - mouseY;
            group.setLayoutX(group.getLayoutX() + deltaX);
            group.setLayoutY(group.getLayoutY() + deltaY);
            mouseX = newMouseX;
            mouseY = newMouseY;
            //was for debugging purposes :)
            //System.out.println("Event: " + event.getX() + " " +event.getY() + " | " + mouseX + " " + mouseY);
        }
    }
}
