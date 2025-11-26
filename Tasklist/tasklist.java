import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

// --------- Model classes ---------

class Task {
    String title;
    boolean done;

    Task(String title, boolean done) {
        this.title = title;
        this.done = done;
    }
}

class TaskList {
    private final List<Task> tasks = new ArrayList<>();
    private final File file;

    TaskList(String filename) {
        this.file = new File(filename);
        load();
    }

    public List<Task> getTasks() {
        return tasks;
    }

    public void addTask(String title) {
        tasks.add(new Task(title, false));
        save();
    }

    public void toggleDone(int index) {
        Task t = tasks.get(index);
        t.done = !t.done;
        save();
    }

    public void deleteTask(int index) {
        tasks.remove(index);
        save();
    }

    public void clearAll() {
        tasks.clear();
        save();
    }

    private void load() {
        tasks.clear();
        if (!file.exists()) {
            return;
        }
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(new FileInputStream(file), StandardCharsets.UTF_8))) {

            String line;
            while ((line = reader.readLine()) != null) {
                // Format: doneFlag;title
                // doneFlag: 0 = not done, 1 = done
                int sepIndex = line.indexOf(';');
                if (sepIndex == -1) continue;

                String flagStr = line.substring(0, sepIndex);
                String title = line.substring(sepIndex + 1);
                boolean done = "1".equals(flagStr);
                tasks.add(new Task(title, done));
            }
        } catch (IOException e) {
            // For a simple app: ignore errors, start with empty list
        }
    }

    private void save() {
        try (BufferedWriter writer = new BufferedWriter(
                new OutputStreamWriter(new FileOutputStream(file), StandardCharsets.UTF_8))) {

            for (Task t : tasks) {
                String flag = t.done ? "1" : "0";
                writer.write(flag + ";" + t.title);
                writer.newLine();
            }
        } catch (IOException e) {
            // For a simple app: ignore save errors
        }
    }
}

// --------- GUI class ---------

public class TaskListApp extends JFrame {

    private final TaskList model;
    private final DefaultListModel<String> listModel = new DefaultListModel<>();

    private final JTextField taskField = new JTextField();
    private final JList<String> taskList = new JList<>(listModel);

    public TaskListApp() {
        super("Task List");
        this.model = new TaskList("tasks.txt");

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 400);
        setLocationRelativeTo(null); // center on screen

        buildUI();
        refreshList();
    }

    private void buildUI() {
        JPanel mainPanel = new JPanel(new BorderLayout(10, 10));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        setContentPane(mainPanel);

        // Top: input + add button
        JPanel topPanel = new JPanel(new BorderLayout(5, 5));
        mainPanel.add(topPanel, BorderLayout.NORTH);

        topPanel.add(taskField, BorderLayout.CENTER);
        JButton addButton = new JButton("Add");
        topPanel.add(addButton, BorderLayout.EAST);

        // Middle: list + scroll
        JScrollPane scrollPane = new JScrollPane(taskList);
        mainPanel.add(scrollPane, BorderLayout.CENTER);

        // Bottom: buttons
        JPanel bottomPanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 5, 5));
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);

        JButton toggleButton = new JButton("Toggle Done");
        JButton deleteButton = new JButton("Delete Task");
        JButton clearButton = new JButton("Clear All");

        bottomPanel.add(toggleButton);
        bottomPanel.add(deleteButton);
        bottomPanel.add(clearButton);

        // List selection mode
        taskList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);

        // Event handlers
        addButton.addActionListener(e -> onAddTask());
        taskField.addActionListener(e -> onAddTask());

        toggleButton.addActionListener(e -> onToggleDone());
        deleteButton.addActionListener(e -> onDeleteTask());
        clearButton.addActionListener(e -> onClearAll());
    }

    private void refreshList() {
        listModel.clear();
        for (Task t : model.getTasks()) {
            String prefix = t.done ? "[✓] " : "[ ] ";
            listModel.addElement(prefix + t.title);
        }
    }

    private int getSelectedIndex() {
        return taskList.getSelectedIndex();
    }

    private void onAddTask() {
        String title = taskField.getText().trim();
        if (title.isEmpty()) {
            JOptionPane.showMessageDialog(this,
                    "Task description cannot be empty.",
                    "Warning",
                    JOptionPane.WARNING_MESSAGE);
            return;
        }
        model.addTask(title);
        taskField.setText("");
        refreshList();
    }

    private void onToggleDone() {
        int index = getSelectedIndex();
        if (index == -1) {
            JOptionPane.showMessageDialog(this,
                    "Select a task first.",
                    "Info",
                    JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        model.toggleDone(index);
        refreshList();
    }

    private void onDeleteTask() {
        int index = getSelectedIndex();
        if (index == -1) {
            JOptionPane.showMessageDialog(this,
                    "Select a task to delete.",
                    "Info",
                    JOptionPane.INFORMATION_MESSAGE);
            return;
        }
        model.deleteTask(index);
        refreshList();
    }

    private void onClearAll() {
        if (model.getTasks().isEmpty()) {
            return;
        }
        int result = JOptionPane.showConfirmDialog(
                this,
                "Delete all tasks?",
                "Confirm",
                JOptionPane.YES_NO_OPTION
        );
        if (result == JOptionPane.YES_OPTION) {
            model.clearAll();
            refreshList();
        }
    }

    public static void main(String[] args) {
        // Make UI look a bit nicer (system look & feel)
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception ignored) {}

        SwingUtilities.invokeLater(() -> {
            TaskListApp app = new TaskListApp();
            app.setVisible(true);
        });
    }
}
