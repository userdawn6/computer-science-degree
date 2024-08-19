public class LandAnimal extends Animals{
    @Override
    String move() {
        return "swinging in tree";
    }

    public static void main(String[] args) {
            LandAnimal lion = new LandAnimal();
            LandAnimal monkey = new LandAnimal();
            monkey.move();
        }
    }
