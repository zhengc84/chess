const getGameOverState = (chess) => {
    if (!chess.isGameOver()) {
        return [false, ''];
    }
    if (chess.isCheckmate()) {
        return [true, 'checkmate'];
    }
    if (chess.isStalemate()) {
        return [true, 'stalemate'];
    }
    if (chess.isThreefoldRepition()) {
        return [true, 'three fold repitition'];
    }
    if (chess.isDraw()) {
        return [true, 'draw'];
    }
};

export default getGameOverState;
