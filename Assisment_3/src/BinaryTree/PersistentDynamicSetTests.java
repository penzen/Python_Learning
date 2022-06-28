package BinaryTree;

import java.awt.*;

public class BalancedSet<E> extends BinarySearchTree<E>{


    /** Color for a red node. */
    protected static final Color RED = Color.red;

    /** Color for a black node. */
    protected static final Color BLACK = Color.black;

    protected  class node extends BinarySearchTree.BinaryTreeNode
    {


        public node(E element) {
            super(element);
        }
    }

    protected void leftRotate(node x)
    {
        node y = (node) x.rightChild;

        // Swap the in-between subtree from y to x.
        x.rightChild = y.leftChild;
        if (y.leftChild != nil)
            y.left.parent = x;

        // Make y the root of the subtree for which x was the root.
        y.parent = x.parent;

        // If x is the root of the entire tree, make y the root.
        // Otherwise, make y the correct child of the subtree's
        // parent.
        if (x.parent == nil)
            root = y;
        else
        if (x == x.parent.left)
            x.parent.left = y;
        else
            x.parent.right = y;

        // Relink x and y.
        y.left = x;
        x.parent = y;
    }
}
