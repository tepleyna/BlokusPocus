import unittest, sys, copy

sys.path.append("../")
sys.path.append("../..")
from BlokusPocus.app.piece import Piece, allShapes

class TestPiece(unittest.TestCase):

    # TODO: shape as text
    # TODO: rotatec rotatecc flipxy shape  (mutate and getter)

    def testSetUp(tp):
        shapes = allShapes()
        pieces = []
        for s in shapes:
            pieces.append(Piece(s, 0))

        tp.assertFalse(len(pieces) == 0)
        tp.assertTrue(len(pieces) == len(shapes))
        for p in pieces:
            with tp.subTest():
                tp.assertIsInstance(p, Piece)

    def testGetIdEqual(tp):
        # after this, we can use getId() in subtests for identity
        id = 12
        p = Piece( [["x"]] , id)
        tp.assertEqual(p.getId(), id)
        tp.assertNotEqual(p.getId(), id+7)

    def testGetShapeEqual(tp):
        shapes = allShapes()

        i = 0
        for shape in shapes:
            i += 1
            with tp.subTest(j = i):
                    p = Piece(shape, i)
                    # not using assertListEqual()because order matters
                    piece_shape = p.getShape()
                    tp.assertEqual(piece_shape, shape)
                    tp.assertNotEqual(piece_shape, [['o']])

    def testShapesNotMutable(tp):
        original_shape = [ ['x','x','o'] ]
        piece = Piece(copy.deepcopy(original_shape), 3) #splicing ensures original is safe

        mutated_copy = piece.getShape()
        mutated_copy[0][1] = 'M'

        piece_shape = piece.getShape()
        tp.assertEqual(piece_shape, original_shape)
        tp.assertNotEqual(piece_shape, mutated_copy)

if __name__ == '__main__':
    unittest.main()
