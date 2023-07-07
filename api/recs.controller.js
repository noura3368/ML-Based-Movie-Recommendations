import recsDAO from "../dao/recsDAO.js" // common pattern to write objects that works with db

export default class RecsController{
    /*
    static async apiPostRecs(req, res, next) {
    try {
        //const recsID= req.body.movieID
        const movie = req.body.movie
        const genres = req.body.genres
        const director = req.body.director
        const cast = req.body.cast
        const response = await recsDAO.getMovie(movie, genres, director, cast)
        res.json({status: "success"})
        }
    catch(e){
            res.status(500).json({error: e.message})
        }
    }
    */

static async apiGetRecs(req, res, next){
    try {
        let movie = req.params.movie || {}
        let recommended_movies = await ReviewsDAO.getReview(movie)
        if (!recommended_movies){
            res.status(404).json({error: "Not found"})
            return
        } 
        res.json(recommended_movies)
    }catch(e) {
        console.log(`api, ${e}`)
        res.status(500).json({error:e})
        }
    }
}