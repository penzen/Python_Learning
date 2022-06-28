Package BinaryTree;

import java.util.HashMap;
import java.util.Map;

/**
 *
 * TO DO: Description
 *
 * @param <E>
 */
public class PersistentDynamicSet<E> extends BinarySearchTree<E> {

    private final Map<Integer, BinaryTreeNode> rootNodes;
    private int version;

    public PersistentDynamicSet() {
        super();
        rootNodes = new HashMap<>();
        version = 1;
    }

    @Override
    protected BinaryTreeNode hookAdd(BinaryTreeNode o) {
        if (o != null) {
            rootNodes.put(version, o);
            version++;
        }
        return o;
    }

    @Override
    protected BinaryTreeNode hookRemove(BinaryTreeNode o) {
        if (o != null) {
            rootNodes.put(version, o);
            version++;
        }
        return o;
    }

    @Override
    protected BinaryTreeNode hookAddTraversed(BinaryTreeNode o) {
        return new BinaryTreeNode(o.element, o.leftChild, o.rightChild, version);
    }

    @Override
    protected BinaryTreeNode versionNode(E o) {
        return new BinaryTreeNode(o, version);
    }

    public Map<Integer, BinaryTreeNode> getRootNodes() {
        Map<Integer, BinaryTreeNode> copy = new HashMap<>(rootNodes);
        copy.put(this.version, this.rootNode);
        return copy;
    }

    @Override
    public BinaryTreeNode getVersionRoot(int version) {
        Map<Integer, BinaryTreeNode> copy = new HashMap<>(rootNodes);
        copy.put(this.version, this.rootNode);
        return copy.get(version);
    }

}