import unittest, sys, copy

sys.path.append("../")
sys.path.append("../..")
from BlokusPocus.app.Piece import Piece, allShapes

class TestPiece(unittest.TestCase):
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
                piece_shape = p.getShape()
                tp.assertEqual(piece_shape, shape)
                tp.assertNotEqual(piece_shape, [['o']])

    def testShapesNotMutable(tp):
        original_shape = [ ['x','x','o'] ]
        piece = Piece(copy.deepcopy(original_shape), 3)

        mutated_copy = piece.getShape()
        mutated_copy[0][1] = 'M'

        piece_shape = piece.getShape()
        tp.assertEqual(piece_shape, original_shape)
        tp.assertNotEqual(piece_shape, mutated_copy)

    def testGetShapeText(tp):
        shapes = [[ ['x'] ] ,
            [['x','x'],
            ['x','o']]]
        expected = [ "x" , "xx\nxo" ]
        for i in range(len(shapes)):
            with tp.subTest(j = i):
                p = Piece(shapes[i], i)
                tp.assertEqual(p.getShapeText(), expected[i])

    def testRotateClockwise(tp):
        shapes = [[ ['x'] ] , #1
            [ ['x','x'] ] ,   #2
            [['x','x'],      #3
            ['x','o'],
            ['x','o']]]
        expected = [[ ['x'] ] ,
            [ ['x'],['x']],
            [['x','x','x'],
            ['o','o','x']]]
        for i in range(len(shapes)):
            with tp.subTest(j = i):
                p = Piece(shapes[i], i)
                tp.assertEqual(p.rotate(True), expected[i])
                tp.assertEqual(p.getShape(), expected[i])

    def testRotateCounterC(tp):
        shapes = [[ ['x'] ] , #1
            [ ['x','x'] ],   #2
            [['x','x'],    #3
            ['x','o']]]
        expected = [[ ['x'] ] ,
            [ ['x'],['x']],
            [['x','o'],
            ['x','x']]]
        for i in range(len(shapes)):
            with tp.subTest(j = i):
                p = Piece(shapes[i], i)
                tp.assertEqual(p.rotate(False), expected[i])
                tp.assertEqual(p.getShape(), expected[i])

    def testFlipX(tp):
        shapes = [[ ['x'] ] , #1
            [ ['x','x'] ],   #2
            [['x','x'],     #3
            ['x','o']]]
        expected = [[ ['x'] ] ,
            [ ['x','x']],
            [['x','o'],
            ['x','x']]]
        for i in range(len(shapes)):
            with tp.subTest(j = i):
                p = Piece(shapes[i], i)
                tp.assertEqual(p.flip(True), expected[i])
                tp.assertEqual(p.getShape(), expected[i])

    def testFlipY(tp):
        shapes = [[ ['x'] ] , #1
            [ ['x','x'] ],   #2
            [['x','x'],     #3
            ['x','o']]]
        expected = [[ ['x'] ] ,
            [ ['x','x']],
            [['x','x'],
            ['o','x']]]
        for i in range(len(shapes)):
            with tp.subTest(j = i):
                p = Piece(shapes[i], i)
                tp.assertEqual(p.flip(False), expected[i])
                tp.assertEqual(p.getShape(), expected[i])

if __name__ == '__main__':
    unittest.main()
